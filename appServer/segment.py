# -*- coding: utf-8 -*-
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
from pydub.utils import mediainfo
import shutil
import glob
from pydub.utils import make_chunks


class Segment():
	def __init__(self, audioPath, audioType):
		self.audioPath = audioPath
		self.audioType = audioType
		self.batchSize = 0
	
	def getSize(self):
		return self.batchSize
	
	def beginSegment(self):
		print('读入音频')
		sound = AudioSegment.from_file(self.audioPath, format=self.audioType)

		# 分割 
		print('开始按句分割')
		#min_silence_len: 拆分语句时，静默满0.25秒则拆分。silence_thresh：小于-50dBFS以下的为静默。
		chunks = split_on_silence(sound,min_silence_len=200,silence_thresh=-40)

		# 创建保存目录
		filepath = os.path.split(self.audioPath)[0]
		chunks_path = filepath+'/chunks/'
		if not os.path.exists(chunks_path):os.mkdir(chunks_path)

		# 保存所有分段
		print('开始保存')
		for i in range(len(chunks)):
			new = chunks[i]
			save_name = chunks_path+'%04d.%s'%(i, 'wav')
			new.export(save_name, format='wav')
			#print('%04d'%(i), len(new))
		print('保存完毕')

		# 把大于2秒的切割
		print ('开始切割大于2秒的音频')
		audiopath1 = chunks_path + '*.wav'
		des_path =  filepath + '/res/'
		if not os.path.exists(des_path):os.mkdir(des_path)

		paths = glob.glob(audiopath1)

		cnt = 1
		for p in range(len(paths)):
			path = paths[p]
			song = mediainfo(path)

			# 大于2秒的文件再切割
			if (float(song['duration']) > 2):
				myaudio = AudioSegment.from_file(path, format='wav')
				chunk_length_ms = 2000 # 分块的毫秒数
				chunks = make_chunks(myaudio, chunk_length_ms) #将文件切割成2秒每块

				#保存切割的音频到文件
				for i, chunk in enumerate(chunks):
					chunk_name = des_path + 'voice_' + str(cnt) + '.wav'
					chunk.export(chunk_name, format="wav")
					cnt = cnt + 1
			else:
				des_path1 = des_path + 'voice_' + str(cnt) + '.wav'
				shutil.move(path, des_path1)
				cnt = cnt + 1

		print("finished")

		# 删除小于0.2秒的音频
		audiopath = des_path + '*.wav'
		paths = glob.glob(audiopath)

		for p in range(len(paths)):
			path = paths[p]
			song = mediainfo(path)
			if (float(song['duration']) < 0.5):
				os.remove(path)

		print("Over")
		paths = glob.glob(audiopath)
		self.batchSize = len(paths)


s = Segment('D:\\learn\\shixun\\appServer\\au.mp3', 'mp3')
s.beginSegment()

