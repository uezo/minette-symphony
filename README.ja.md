# Minette adapter for Symphony

Minetteフレームワークを使用したチャットボットをSymphonyに接続するためのアダプター。


# インストール

```
$ pip install minette-symphony
```


# おうむ返しBOTのサンプル

動作確認用のおうむ返しBOTはとても簡単に作ることができます。

```python
from minette import DialogService
from minette_symphony import SymphonyAdapter

# Custom dialog service (echo)
class MyDialog(DialogService):
    def compose_response(self, request, context, connection):
        # request.text is plain text message parsed from XML message from Symphony.
        # request.channel_message contains the whole event data.
        return "You said: " + request.text

# Create adapter. Bot instance is also created internally.
adapter = SymphonyAdapter(
    # symphony.json is the config file for Symphony SDK
    symphony_config="symphony.json",
    default_dialog_service=MyDialog,
    prepare_table=True,
    debug=True)

# Start datafeed
adapter.start_datafeed()
```


# 詳細情報

フレームワークの詳細な機能やスキルの追加方法などは [Minette](https://github.com/uezo/minette-python) を参照してください。

