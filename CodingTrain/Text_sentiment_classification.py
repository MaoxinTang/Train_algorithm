def get_sentiment(sentence):
  sum_score = 0
  # 用空格切分句子，并遍历分割出的每个词语
  for word in sentence.split():
    # 尝试获取 word 对应的情感值
    score = senti_dict.get(word)
    # 若返回值不为 None，说明该词语在情感词典中，累计得分
    if score:
      sum_score += score
  # 情感得分为负，说明句子情感极性是消极的
  if sum_score < 0:
    return '消极'
  # 否则为积极的
  else:
    return '积极'