# Impor library yang dibutuhkan
import openai
import os
import base64
from PIL import Image
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def visualize_concept(topic: str) -> Image.Image:
    print(f"🎨 Tool 'visualize_concept' dipanggil dengan topik: {topic}")
    
    enhanced_prompt = f"A clear, minimalist, and professional diagram explaining the concept of '{topic}'. Tech-style infographic, white background, simple icons."

    try:
        image_response = openai.images.generate(
            model="dall-e-3",
            prompt=enhanced_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            response_format="b64_json",
        )
        
        image_base64 = image_response.data[0].b64_json
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        return image

    except openai.OpenAIError as e:
        print(f"❌ Error saat memanggil DALL-E 3: {e}")
        return Image.new('RGB', (512, 512), color = 'red')

def talker(message: str):
    print("📢 Tool 'talker' dipanggil untuk mengucapkan pesan.")
    plain_text = message.replace('*', '').replace('`', '').replace('**', '').replace('```', '').replace("###", "").replace("##", "").replace("#", "").strip()

    try:
        response = openai.audio.speech.create(
          model="tts-1",
          voice="onyx",
          input=plain_text
        )

        audio_stream = BytesIO(response.content)
        audio = AudioSegment.from_file(audio_stream, format="mp3")
        
        print("✅ Audio berhasil dibuat, sedang memutar...")
        play(audio)

    except openai.OpenAIError as e:
        print(f"❌ Error saat memanggil TTS API: {e}")