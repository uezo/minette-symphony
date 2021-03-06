# Minette adapter for Symphony

Adapter for Symphony to create chatbot using Minette framework.


# Installation

```
$ pip install minette-symphony
```


# Running the echo bot

Running echo bot is extremely easy.

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


# More details

See also [Minette](https://github.com/uezo/minette-python) to understand the features of this framework and how to add your own skills.

