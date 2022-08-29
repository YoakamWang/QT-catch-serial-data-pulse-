import os.path

cur_path = os.path.dirname(__file__)
ab_path=os.path.abspath(__file__)
with open(ab_path, 'r') as fd:
    print('done')
