from typing import List


def get_categories(des: str) -> List:
  TYPES = ['Exploratory', 'Concentration']
  categories = ['Core', 'Seminar', 'Experiential Learning']
  for t in TYPES:
    for i in range(4):
      categories.append(f'{t[0]}{i+1}')

  ret = []  
  try:
    category = des.split('Category: ')[1].split('\n')[0]
  except:
    print(f'=> ERROR while getting categories')
    return []
  
  for token in categories:
    if token in category:
      ret.append('EL' if token == 'Experiential Learning' else token)
  
  return ret

def get_schedule(schedule_text: str) -> List:
	schedule = []
	print(schedule_text.split('\n'))
	blocks = schedule_text.split('\n')
	for block in blocks:
		if not (':' in block):
			continue
		tokens = block.split()
		for day in tokens[2:]:
			schedule.append({
				'day': day.strip(','),
				'start_time': tokens[0],
				'end_time': tokens[1]
			})
	
	return schedule