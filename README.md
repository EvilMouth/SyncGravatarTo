# SyncGravatarTo
sync gravatar to ...

**一键同步Gravatar头像到各平台**
- Twitter
- Telegram
- v2ex
- ...

## 使用说明
配置`property.json`文件后运行`main.py`即可
> key请自行保管


``` json
property.json

{
  "mainEmail": "izyhang@gmail.com",
  "twitter": {
    "enable": true,
    "consumer_key": "",
    "consumer_secret": "",
    "token_key": "",
    "token_secret": ""
  },
  "telegram": {
    "enable": true,
    "api_id": "",
    "api_hash": "",
    "email": "izyhang@qq.com"
  }
}
```
