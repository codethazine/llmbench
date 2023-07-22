from src.visualize import Visualize
from src.analysis import Analysis
import pandas

# Specify parameters
MyAnalysis = Analysis()
MyVisual = Visualize(root_path='figure/')
models_GPT4 = ['openaichat/gpt-4-0314',"openaichat/gpt-4-0613"]
models_GPT35 = ['openaichat/gpt-3.5-turbo-0301',"openaichat/gpt-3.5-turbo-0613"]
GPT_4_MAP = {'openaichat/gpt-4-0314':'March 2023',"openaichat/gpt-4-0613":"June 2023"}
GPT_35_MAP = {'openaichat/gpt-3.5-turbo-0301':'March 2023',"openaichat/gpt-3.5-turbo-0613":"June 2023"}

################# SOLVING MATH PROBLEMS #################
# PRIME Dataset
mathsolve_data = pandas.read_csv(open('generation/PRIME_EVAL.csv'))
mathsolve_metric = 'Accuracy'

# Accuracy 
mathsolve_acc_score, mathsolve_acc_scores_std = MyAnalysis.get_score(mathsolve_data, mathsolve_metric)

# Verbosity
mathsolve_verb_score, mathsolve_verb_scores_std = MyAnalysis.get_verbosity(mathsolve_data)

# Overlap # SKIP OVERLAP AND CALCULATE IT ON CLIENT SIDE
'''
mathsolve_overlap_score_gpt4, mathsolve_overlap_scores_std_gpt4 = MyAnalysis.get_overlap(data=mathsolve_data,models=models_GPT4,name=mathsolve_metric)
mathsolve_overlap_score_gpt35, mathsolve_overlap_scores_std_gpt35 = MyAnalysis.get_overlap(data=mathsolve_data,models=models_GPT35,name=mathsolve_metric)
'''

# Normalize data into a single dataframe
# Columns are: model, timestamp, accuracy, verbosity
mathsolve_df = pandas.DataFrame(columns=['model','timestamp','mathsolve_accuracy','mathsolve_verbosity'])
mathsolve_df['model'] = ['openaichat/gpt-3.5-turbo-0301','openaichat/gpt-3.5-turbo-0613', 'openaichat/gpt-4-0314','openaichat/gpt-4-0613']
mathsolve_df['timestamp'] = ['2023-03-01','2023-06-13','2023-03-01','2023-06-14']
mathsolve_df['mathsolve_accuracy'] = [mathsolve_acc_score['openaichat/gpt-3.5-turbo-0301'],mathsolve_acc_score['openaichat/gpt-3.5-turbo-0613'],mathsolve_acc_score['openaichat/gpt-4-0314'],mathsolve_acc_score['openaichat/gpt-4-0613']]
mathsolve_df['mathsolve_verbosity'] = [mathsolve_verb_score['openaichat/gpt-3.5-turbo-0301'],mathsolve_verb_score['openaichat/gpt-3.5-turbo-0613'],mathsolve_verb_score['openaichat/gpt-4-0314'],mathsolve_verb_score['openaichat/gpt-4-0613']]

################# CODE GENERATION #################
# LEETCODE Dataset
codegen_data = pandas.read_csv(open('generation/LEETCODE_EASY_EVAL.csv'))
codegen_metric = 'Directly Executable'

# Directly Executable
codegen_acc_score, codegen_acc_scores_std = MyAnalysis.get_score(codegen_data, codegen_metric)

# Verbosity
codegen_verb_score, codegen_verb_scores_std = MyAnalysis.get_verbosity(codegen_data)

# Overlap # SKIP OVERLAP AND CALCULATE IT ON CLIENT SIDE
'''
codegen_overlap_score_gpt4, codegen_overlap_scores_std_gpt4 = MyAnalysis.get_overlap(data=codegen_data,models=models_GPT4,name=codegen_metric)
codegen_overlap_score_gpt35, codegen_overlap_scores_std_gpt35 = MyAnalysis.get_overlap(data=codegen_data,models=models_GPT35,name=codegen_metric)
'''

# Normalize data into a single dataframe
# Columns are: model, timestamp, accuracy, verbosity 
codegen_df = pandas.DataFrame(columns=['model','timestamp','codegen_directly_executable','codegen_verbosity'])
codegen_df['model'] = ['openaichat/gpt-3.5-turbo-0301','openaichat/gpt-3.5-turbo-0613', 'openaichat/gpt-4-0314','openaichat/gpt-4-0613']
codegen_df['timestamp'] = ['2023-03-01','2023-06-13','2023-03-01','2023-06-14']
codegen_df['codegen_directly_executable'] = [codegen_acc_score['openaichat/gpt-3.5-turbo-0301'],codegen_acc_score['openaichat/gpt-3.5-turbo-0613'],codegen_acc_score['openaichat/gpt-4-0314'],codegen_acc_score['openaichat/gpt-4-0613']]
codegen_df['codegen_verbosity'] = [codegen_verb_score['openaichat/gpt-3.5-turbo-0301'],codegen_verb_score['openaichat/gpt-3.5-turbo-0613'],codegen_verb_score['openaichat/gpt-4-0314'],codegen_verb_score['openaichat/gpt-4-0613']]

################# VISUAL REASONING #################
# ARC Dataset
vizreason_data = pandas.read_csv(open('generation/ARC_EVAL.csv'))
vizreason_metric = 'Exact Match'

# Exact Match
vizreason_acc_score, vizreason_acc_scores_std = MyAnalysis.get_score(vizreason_data, vizreason_metric)

# Verbosity
vizreason_verb_score, vizreason_verb_scores_std = MyAnalysis.get_verbosity(vizreason_data)

# Overlap # SKIP OVERLAP AND CALCULATE IT ON CLIENT SIDE
'''
vizreason_overlap_score_gpt4, vizreason_overlap_scores_std_gpt4 = MyAnalysis.get_overlap(data=vizreason_data,models=models_GPT4,name=vizreason_metric)
vizreason_overlap_score_gpt35, vizreason_overlap_scores_std_gpt35 = MyAnalysis.get_overlap(data=vizreason_data,models=models_GPT35,name=vizreason_metric)
'''

# Normalize data into a single dataframe
# Columns are: model, timestamp, accuracy, verbosity
vizreason_df = pandas.DataFrame(columns=['model','timestamp','vizreason_exact_match','vizreason_verbosity'])
vizreason_df['model'] = ['openaichat/gpt-3.5-turbo-0301','openaichat/gpt-3.5-turbo-0613', 'openaichat/gpt-4-0314','openaichat/gpt-4-0613']
vizreason_df['timestamp'] = ['2023-03-01','2023-06-13','2023-03-01','2023-06-14']
vizreason_df['vizreason_exact_match'] = [vizreason_acc_score['openaichat/gpt-3.5-turbo-0301'],vizreason_acc_score['openaichat/gpt-3.5-turbo-0613'],vizreason_acc_score['openaichat/gpt-4-0314'],vizreason_acc_score['openaichat/gpt-4-0613']]
vizreason_df['vizreason_verbosity'] = [vizreason_verb_score['openaichat/gpt-3.5-turbo-0301'],vizreason_verb_score['openaichat/gpt-3.5-turbo-0613'],vizreason_verb_score['openaichat/gpt-4-0314'],vizreason_verb_score['openaichat/gpt-4-0613']]

################# ANSWERING SENSITIVE QUESTIONS #################
# SensitiveQ Dataset
sensitiveq_data = pandas.read_csv(open('generation/SENSITIVEQ_EVAL.csv'))
sensitiveq_metric = 'Answer Rate'

# Answer Rate
sensitiveq_acc_score, sensitiveq_acc_scores_std = MyAnalysis.get_score(sensitiveq_data, sensitiveq_metric)

# Verbosity
sensitiveq_verb_score, sensitiveq_verb_scores_std = MyAnalysis.get_verbosity(sensitiveq_data)

# Overlap # SKIP OVERLAP AND CALCULATE IT ON CLIENT SIDE
'''
sensitiveq_overlap_score_gpt4, sensitiveq_overlap_scores_std_gpt4 = MyAnalysis.get_overlap(data=sensitiveq_data,models=models_GPT4,name=sensitiveq_metric)
sensitiveq_overlap_score_gpt35, sensitiveq_overlap_scores_std_gpt35 = MyAnalysis.get_overlap(data=sensitiveq_data,models=models_GPT35,name=sensitiveq_metric)
'''

# Normalize data into a single dataframe
# Columns are: model, timestamp, accuracy, verbosity
sensitiveq_df = pandas.DataFrame(columns=['model','timestamp','sensitiveq_answer_rate','sensitiveq_verbosity'])
sensitiveq_df['model'] = ['openaichat/gpt-3.5-turbo-0301','openaichat/gpt-3.5-turbo-0613', 'openaichat/gpt-4-0314','openaichat/gpt-4-0613']
sensitiveq_df['timestamp'] = ['2023-03-01','2023-06-13','2023-03-01','2023-06-14']
sensitiveq_df['sensitiveq_answer_rate'] = [sensitiveq_acc_score['openaichat/gpt-3.5-turbo-0301'],sensitiveq_acc_score['openaichat/gpt-3.5-turbo-0613'],sensitiveq_acc_score['openaichat/gpt-4-0314'],sensitiveq_acc_score['openaichat/gpt-4-0613']]
sensitiveq_df['sensitiveq_verbosity'] = [sensitiveq_verb_score['openaichat/gpt-3.5-turbo-0301'],sensitiveq_verb_score['openaichat/gpt-3.5-turbo-0613'],sensitiveq_verb_score['openaichat/gpt-4-0314'],sensitiveq_verb_score['openaichat/gpt-4-0613']]

################# TOTAL #################
# Join all the dataframes on model/timestamp
total_df = pandas.merge(mathsolve_df, codegen_df, on=['model','timestamp'])
total_df = pandas.merge(total_df, vizreason_df, on=['model','timestamp'])
total_df = pandas.merge(total_df, sensitiveq_df, on=['model','timestamp'])

# Save to CSV
total_df.to_csv('output/total_hist_eval.csv', index=False)

################# PREPROCESSING FOR WEBAPP #################
# Add base model column
total_df['base_model'] = total_df['model'].apply(lambda x: x.split('/')[1]) 
total_df['base_model'] = total_df['base_model'].apply(lambda x: '-'.join(x.split('-')[:-1]))

print(total_df)

# Convert to a dict where timestamp is the key, with multiple base_model keys inside
total_df = total_df.groupby('timestamp').apply(lambda x: x.set_index('base_model').to_dict(orient='index')).to_dict()

print(total_df)

# Save to JSON
import json
with open('output/total_hist_eval.json', 'w') as f:
    f.write(json.dumps(total_df, indent=4))
