#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib
import json

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives._serialization import Encoding
from cryptography.hazmat.primitives._serialization import PublicFormat
import requests

# @Author  : pengchen
# @Time    : 2023年10月10日
# @Function: 本范例代码，可以通过修改参数，运行main函数，查看接口效果
#  pip3 install cryptography
#  pip3 install pycryptodome

# 自动发布接口域名
DOMAIN = "http://api.developer.xiaomi.com/devupload"

# 推送普通apk Url前缀
PUSH = DOMAIN + "/dev/push"

# 本地公钥文件地址
PUBLIC_CER = "/Users/wangtao/Documents/stores/xiaomi.dev.api.public.cer"

# 查询app状态的Url前缀
QUERY = DOMAIN + "/dev/query"

# 查询应用分类Url前缀
CATEGORY = DOMAIN + "/dev/category"

# 以下三项为接口参数加密算法X509用到的参数
KEY_SIZE = 1024
GROUP_SIZE = 128
ENCRYPT_GROUP_SIZE = GROUP_SIZE - 11


# 公钥加密函数
def encrypt_by_public_key(param):
    with open(PUBLIC_CER, 'rb') as f:
        buff = f.read()
    cert_obj = load_pem_x509_certificate(buff, default_backend())
    public_key = cert_obj.public_key()
    pk = public_key.public_bytes(encoding=Encoding.PEM, format=PublicFormat.PKCS1)
    cipher_public = PKCS1_v1_5.new(RSA.importKey(pk))

    text_bytes = param.encode('UTF-8')
    text_bytes_len = len(text_bytes)
    idx = 0
    encrypt_bytes = bytearray()
    while idx < text_bytes_len:
        remain = text_bytes_len - idx
        if remain > ENCRYPT_GROUP_SIZE:
            segsize = ENCRYPT_GROUP_SIZE
        else:
            segsize = remain
        segment = bytearray(segsize)
        array_copy(text_bytes, idx, segment, 0, segsize)
        encrypt_bytes = encrypt_bytes + cipher_public.encrypt(segment)
        idx += segsize
    return encrypt_bytes.hex()


def array_copy(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]


# 获取文件的md5
def get_file_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()


# 查询应用分类
def get_categories():
    response = requests.post(CATEGORY)
    return response.text


# 查询应用信息，前提是小米开放平台已经创建了包名
def query(email, password, package_name):
    request_data = {
        "packageName": package_name,
        "userName": email
    }
    sig = {
        "sig": [
            {
                "name": "RequestData",
                "hash": hashlib.md5(json.dumps(request_data).encode()).hexdigest()
            }
        ],
        "password": password
    }
    encrypted_sig = encrypt_by_public_key(json.dumps(sig))
    response = requests.post(QUERY, data={"RequestData": json.dumps(request_data), "SIG": encrypted_sig})
    return response.text


# 推送应用  synchro_type 0：新增app; 1：更新app; 2：app信息修改
def push(email, password, synchro_type, apk_file, icon_file, app_detail, screenshots):
    request_data = {
        "userName": email,
        "appInfo": json.dumps(app_detail),
        "synchroType": synchro_type
    }

    # Calculate digital signature
    sig_json = {
        "sig": [],
        "password": password
    }

    sig_item = {
        "name": "RequestData",
        "hash": hashlib.md5(json.dumps(request_data).encode('utf-8')).hexdigest()
    }

    sig_json["sig"].append(sig_item)

    if apk_file is not None:
        apk = {
            "name": "apk",
            "hash": get_file_md5(apk_file)
        }
        sig_json["sig"].append(apk)

    if icon_file is not None:
        icon = {
            "name": "icon",
            "hash": get_file_md5(icon_file)
        }
        sig_json["sig"].append(icon)

    if screenshots is not None and len(screenshots) > 0:
        for i in range(len(screenshots)):
            screenshot_name = "screenshot_" + str(i + 1)
            screenshot = {
                "name": screenshot_name,
                "hash": get_file_md5(screenshots[i])
            }
            sig_json["sig"].append(screenshot)

    encrypted_sig = encrypt_by_public_key(json.dumps(sig_json))

    files = {
        "apk": (os.path.basename(apk_file), open(apk_file, "rb")),
        "icon": (os.path.basename(icon_file), open(icon_file, "rb")),
    }
    for i in range(len(screenshots)):
        files[f"screenshot_{i + 1}"] = (os.path.basename(screenshots[i]), open(screenshots[i], "rb"))

    response = requests.post(PUSH, data={"RequestData": json.dumps(request_data), "SIG": encrypted_sig}, files=files)
    return response.text


# 小米账号邮箱
email = "18334770485@163.com"
# 小米账号私钥
password = "knirx35yrmcmzlf42m79z53jy60ioxdgo6l25ffcvftj05eyv6"
# 测试包名
package_name = "com.beings.aiu"


if __name__ == '__main__':
    # 调用查询分类函数
    # print(get_categories())
    # 调用查询函数
    # print(query(email, password, package_name))

    app_detail = {
        "appName": "AiU-智能AI聊天兴趣社区",
        "packageName": package_name,
        "updateDesc": "1、修复部分问题\n2、优化用户体验",
        "privacyUrl": "https://aiu.ai-topia.com/resource/privacy.html",
    }

    apk_file = "apk文件路径"
    icon_file = "icon文件路径"

    # 提交普通apk包
    result = push(email, password, 1, apk_file, icon_file, app_detail, None)
    print(f"结果[{result}]")
