from Crypto.Cipher import AES
import base64
import string
import random
import json


class AESCrypto(object):
    """AES加密算法"""

    def __init__(self):
        self.aes_mode = AES.MODE_ECB
        self.aes_bs = 16
        self.AES_PAD = lambda s: s + (self.aes_bs - len(s) % self.aes_bs) * chr(self.aes_bs - len(s) % self.aes_bs)
        self.AES_UN_PAD = lambda s: s[0:-s[-1]]

    def aes_decryption(self, data, key):
        """
        aes解密
        解密后，将补足的空格用strip() 去掉
        :param data: 接收到的密文数据集合
        :param key: 服务端返回的随机生成的AESKey,二进制形式
        :return: aes解密后的明文数据
        """
        generator = AES.new(key, self.aes_mode)  # ECB模式无需向量iv
        data += (len(data) % 4) * '='
        decrypt_bytes = base64.b64decode(data)
        result = generator.decrypt(decrypt_bytes)
        result = self.AES_UN_PAD(result)
        result = str(result, encoding="utf-8")  # 转换类型
        # 去除解码后的非法字符
        return result

    def aes_encryption(self, data, key):
        """
        aes加密
        如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
        :param data: 要上传的所有明文数据集合，包含sign
        :param key:  本地随机生成的AESKey，字符串形式
        :return: aes加密后的密文数据
        """
        generator = AES.new(key, self.aes_mode)  # ECB模式无需向量iv
        crypt = generator.encrypt(self.AES_PAD(data))
        encrypt_str = base64.b64encode(crypt)
        result = encrypt_str.decode()
        return result

    @classmethod
    def aes_encrypt_key(cls):
        """随机生成AESKey"""
        source_str = string.ascii_letters + string.digits
        aes_key = "".join(random.sample(source_str, 16))
        return aes_key


if __name__ == '__main__':
    aes = AESCrypto()
    key = "450fb354063c3276"
    # strs = "1235123"
    # mw = aes.aes_encryption(strs, key)
    jie = aes.aes_decryption(
        "5tyIHTi8Qtg+ZZy64ZsX46ltT4LtN4+2oePMzh+3ETy7QfI4D3jH8tPuOfq7QgRJMnoL73NzJUP7ZjNWwCS8j9tR2RyNhll+l7THo8WicejrTP0fxNr44h9WDr0B8ugt2/3nLs2GMRchzsZmCSex+YuVUsqkTpRPPfy0T1LhH1q+ceNzGXvLuCXbOhkjRjSgK2usD5M2H9ocOaJ+e/Y97RtqpMa0D5QnuGvm5i4f29gsyL8zyqKB8iXz2VxVnd5DRtMAXqDHWUT99wh2DW0dE07J1wFBh5w9LS5ph1doTkB+7USdlow8cKspuXl1dF/6/9nJdC9d+ZJCB5v8gnb51SDo9Ke85oP04yBH1INRO2geBRdogozO9eSqSsxjTaweGEFyZauY4V3vMD2R178g0+pd/XObn60MbvxmA1BM6Kco549IBB0XkIDL+8kBILtlXdbXgRpwxoYQqrNQhb4S66wJZ//nIF1XnvNgb03+rtnELMQaKfNttSdTgXGh0zWZMj/fZ5vVimKXNVj65w39xvFXIHu8FLAEIm87CcXtlLNH2bQOpondmxNaDCN043s0DJLoB6hCLTs/OskKd0lirS95skRIvzDkqFViv5Kg9IArNKPS3P54logSuVjpapcNveD5v+Em5hTHGOLir3s8xI8d/QjXgmtgKrS5C3OUZyqH5/F2N661IjERreQvCAb6I3TjbGFL64/VSMdqJ+xnKcJlqsvQv1rr8/kvZDTLrzEvY+xUtL4Bo2i/0ElKpsTYntbAkL+/JOX+9bHVa9eKqzSW2B2bRZ0dpmBFKQnUOK3zgXFyXNo0+26tD8x3Tk0OZmAD8xr16vdK+WlkSC1u7wtsSfv2NgXd8awDVXVyHJXQHbxf+xBMsACACTHbo67sKSjC+/pNQH5ENYP/p9OT2eHu7BD/D+FQWoTDz8pDp8Dd/70nfjJ6Uzg3jZAMmDJvbqSeeux4CivcaEx1NWr5P+R05kzZDteAcomuNzkOhbzP99MCDPGOy5/WG/s03aYVjcw/MOGi9t95A5Pm8g7lz1vmZaLvn7x+BhjmYIhJFVNy683jDCeuubzzbsjbKPiwzhCYH3WSAWKzKU22Y/L99A5tkewZ5/HWioypOJFXsP9UZU0dGJka2Xn6D1OIoDxS6PbWz9IbrWnMDUJ00DkFxvM/z7sV23j21lrBEegf5I9Ug80Q+IlWWvatFgQ/uJy7+NXOm+PT5R7149bG9i7gmfpm8p+GWz+bMNPuKAdAWM1HoNkH4GEYpIBAslcKCYs6QkLilgGZSbWBMT1wzrKTB/okhi9Jp2PDycYXsbNcPR4ObZHsGefx1oqMqTiRV7D/ixGi+J2kgh1oeYdDiCZfOs/1AsiiU7mPWJ/1dOBrrLn3BawM+H5uBQD6u9XBKW26xEwfDO37Nsjw8GMXiXnPwglgW7MTOY9vmC4uMolWxISuQ1+GnRzA1skoMGvKXFK5",
        key)
    print(jie)
