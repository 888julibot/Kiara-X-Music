FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

# Install dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Add the banall function
RUN echo "from telethon.tl.functions.channels import EditBannedRequest, DeleteMessagesRequest" >> your_file_with_event_handlers.py
RUN echo "from telethon.tl.types import ChatBannedRights" >> your_file_with_event_handlers.py
RUN echo "from telethon.errors import rpcerrorlist" >> your_file_with_event_handlers.py
RUN echo "" >> your_file_with_event_handlers.py
RUN echo "@sree.on(events.NewMessage(pattern='^/banall'))" >> your_file_with_event_handlers.py
RUN echo "async def banall(event):" >> your_file_with_event_handlers.py
RUN echo "    if event.sender_id in OP:" >> your_file_with_event_handlers.py
# ... add the rest of your banall function code ...

# Start the bot
CMD bash start
