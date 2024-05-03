####执行代码####
##工具包安装##
pip install moviepy
##下载视频##
yt-dlp -f 'bv' URL
##下载音频##
yt-dlp -f 'ba' URL

from moviepy.editor import VideoFileClip, AudioFileClip

# 视频和音频文件路径
video_path = f'C:\\Users\\User\\Desktop\\茜茜\\舒曼.mp4'
audio_path = f'C:\\Users\\User\\Desktop\\茜茜\\舒曼.m4a'

# 加载视频和音频文件
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)

# 设置音频剪辑到视频剪辑（替换原有音频）
video_clip = video_clip.set_audio(audio_clip)

# 输出文件路径
output_path = '舒曼3.mp4'

# 写入合并后的文件
video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
