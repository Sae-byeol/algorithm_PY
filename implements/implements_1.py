# 소프티어 - 전광판 (Lv2)
import sys 
std = sys.stdin;

k = int(std.readline());
input_array =[]
for i in range(k):
  input_array.append(list(map(int, std.readline().split(' '))));

num_dict ={
  0: [0,1,4,5,6,3],
  1: [3,6],
  2: [0,3,2,4,5],
  3: [0,2,3,6,5],
  4: [1,2,3,6],
  5: [0,1,2,6,5],
  6: [0,1,2,4,5,6],
  7: [1,0,3,6],
  8: [0,1,2,3,4,5,6], 
  9: [0,1,2,3,6,5]
}

for input in input_array:
  start = list(map(int, str(input[0])))
  end = list(map(int, str(input[1])))
  start_len= len(start);
  end_len= len(end);
  # start, end 길이 같도록.
  if (start_len > end_len):
    for i in range(0, start_len - end_len):
      end.insert(0,-1);
  elif (end_len > start_len):
     for i in range(0, end_len - start_len):
      start.insert(0,-1);
  #한자리씩 비교 시작
  answer =0;

  for i in range(0, len(start)):
    start_cur = start[i];
    end_cur = end[i];
    #둘 중 하나가 -1인 경우
    if (start_cur == -1):
      answer = answer + len(num_dict[end_cur]);
      continue;
    elif (end_cur == -1):
      answer = answer + len(num_dict[start_cur]);
      continue;
    #start_cur -> end_cur 바뀌어야하는 부분 개수 찾기
    start_dict = num_dict[start_cur];
    end_dict = num_dict[end_cur];
    diff_1 = list(set(start_dict) - set(end_dict));
    diff_2 = list(set(end_dict) - set(start_dict));
    answer = answer + len(diff_1) + len(diff_2);
  print(answer); 
    