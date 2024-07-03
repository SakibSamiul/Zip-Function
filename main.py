names = ["Sakib", "Samiul", "Sharika","Shamima","Smriti"]
marks = [97, 77, 99, 90, 98]
subjects = ["Math", "Chemistry", "English", "Science", "Math"]

for name,mark,subject in zip(names, marks, subjects):
  print(name,"has scored",mark,"marks in",subject)