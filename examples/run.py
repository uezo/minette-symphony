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
    symphony_config="symphony.json",
    default_dialog_service=MyDialog,
    prepare_table=True,
    debug=True)

# Start datafeed
adapter.start_datafeed()
