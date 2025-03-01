#!/usr/bin/env python3
import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your actual group IDs (negative numbers for supergroups)
SOURCE_CHAT_ID = -xxxxxxxxx   # The group/channel to monitor
DESTINATION_CHAT_ID = -xxxxxxxx  # The group/channel to re-post into

def replicate_message(update: Update, context: CallbackContext):
    """
    Re-sends the message content from SOURCE_CHAT_ID to DESTINATION_CHAT_ID.
    This method creates a new message (text, photo, etc.) so that the original sender
    information ("Forwarded from") is not shown.
    """
    message = update.effective_message

    # Process only messages from the source chat
    if message.chat_id == SOURCE_CHAT_ID:
        try:
            # Check for photo messages
            if message.photo:
                # Use the highest-resolution photo (last in the list)
                photo_file_id = message.photo[-1].file_id
                caption = message.caption if message.caption else ""
                context.bot.send_photo(
                    chat_id=DESTINATION_CHAT_ID,
                    photo=photo_file_id,
                    caption=caption
                )
            # Check for video messages
            elif message.video:
                video_file_id = message.video.file_id
                caption = message.caption if message.caption else ""
                context.bot.send_video(
                    chat_id=DESTINATION_CHAT_ID,
                    video=video_file_id,
                    caption=caption
                )
            # Check for document messages
            elif message.document:
                doc_file_id = message.document.file_id
                caption = message.caption if message.caption else ""
                context.bot.send_document(
                    chat_id=DESTINATION_CHAT_ID,
                    document=doc_file_id,
                    caption=caption
                )
            # Check for audio messages
            elif message.audio:
                audio_file_id = message.audio.file_id
                caption = message.caption if message.caption else ""
                context.bot.send_audio(
                    chat_id=DESTINATION_CHAT_ID,
                    audio=audio_file_id,
                    caption=caption
                )
            # Check for voice messages
            elif message.voice:
                voice_file_id = message.voice.file_id
                context.bot.send_voice(
                    chat_id=DESTINATION_CHAT_ID,
                    voice=voice_file_id
                )
            # Check for video notes
            elif message.video_note:
                video_note_file_id = message.video_note.file_id
                context.bot.send_video_note(
                    chat_id=DESTINATION_CHAT_ID,
                    video_note=video_note_file_id
                )
            # Check for sticker messages
            elif message.sticker:
                sticker_file_id = message.sticker.file_id
                context.bot.send_sticker(
                    chat_id=DESTINATION_CHAT_ID,
                    sticker=sticker_file_id
                )
            # Check for plain text messages
            elif message.text:
                context.bot.send_message(
                    chat_id=DESTINATION_CHAT_ID,
                    text=message.text
                )
            else:
                logger.info("Received message type not handled; skipping.")

            logger.info("Re-sent a message from chat %s to %s", SOURCE_CHAT_ID, DESTINATION_CHAT_ID)
        except Exception as e:
            logger.error("Error while re-sending message: %s", e)

def main():
    # Your bot token (replace with your actual token)
    TOKEN = "YOUR TELEGRAM BOT API"
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handle all messages from the source chat
    dp.add_handler(MessageHandler(Filters.all, replicate_message))

    # Start polling for updates from Telegram
    updater.start_polling()
    logger.info("Bot started. Listening for messages in chat %s", SOURCE_CHAT_ID)
    
    # Run the bot until Ctrl+C is pressed
    updater.idle()

if __name__ == '__main__':
    main()
