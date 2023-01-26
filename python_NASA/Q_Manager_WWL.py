import pandas as pd
import datetime
import os
from NASA_TLX_WWL import TLX
# from minimal_self import MINIMALSELFA
# from mental_distance import MENTAL_DISTANCE
# from subjective_evaluation import SUBJECTIVE_EVALUATION

def initial_data_set():
	name = input('名前を入力してください--> ')
	job = input('操作人数は？\n1人->1\n2人-->2\n3人-->3\n')
	# number = input('サイクル数を入力してください--> ')
	return name, job

def write(path,data):
	df = pd.DataFrame(data.values(), index=data.keys()).T
	exportPath = path + 'questionnaire' + '_' + name + '_' + job + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M') + '.csv'
	df.to_csv(exportPath)
				
if __name__ == '__main__':
	name,job = initial_data_set()

	TLX_manager = TLX()
	# MINIMALSELF_manager = MINIMALSELF()
	# MENTALDISTANCE_manager = MENTAL_DISTANCE()
	# SUBJECTIVEEVALUATION_manager = SUBJECTIVE_EVALUATION()

	r_tlx = TLX_manager.main()
	# r_MS = MINIMALSELF_manager.main()
	# r_MD = MENTALDISTANCE_manager.main()
	# r_SE = SUBJECTIVEEVALUATION_manager.main()
	# r_Q = r_tlx|r_MS|r_MD|r_SE
	r_Q = r_tlx

	# ---------- change where u save data ---------- #
	write(os.path.join('GraduationThesis/zikken',''),r_Q) # 実行ファイルと同じ階層にファイル作成，/でさらに下層に保存可能，例)GraduationThesis/example
	# write(os.path.join('/Users/sanolab/Desktop/NASA',''),r_Q) # 実行ファイルと同じ階層にファイル作成，/でさらに下層に保存可能，例)GraduationThesis/example