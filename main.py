# Part 1
def read_csv(filename):
  """
  This function takes a string "filename" and reads the CSV data stored in it. Then the function returns two values "(header,data)", for which "header" is a list containing the column labels and "data" is a nested list containing the rest of the data

  Parameters
  ----------
  filename:
    The name of a file in string

  Returns
  -------
  list:
    Header containing the column labels of the file

  list:
    Data contains the rest of the data

  Examples
  ----------
  >>> read_csv("grades.csv")
  ['grade', 'score']
  [['A', '70'],
   ['B', '60'],
   ['C', '55'],
   ['D', '50'],
   ['E', '45'],
   ['S', '40'],
   ['U', '0']]
  """
  with open(filename,'r') as f:
    datas = f.readlines()
    data = []
    header = []
    for d in datas:
      clean_data = d.strip("\n")
      clean_data_list = clean_data.split(",")
      if "year" not in d:
        individual_data = []
        for info in clean_data_list:
          if info.isdigit():
            individual_data.append(int(info))
          else:
            individual_data.append(str(info))
        data.append(individual_data)
      else:
        for head in clean_data_list:
          header.append(head)
  return header,data

def filter_gender(enrolment_by_age, sex): 
  """
  This function takes a list of recored "enrolment_by_age" and a string "sex". This function then returns a list of records where the value in the "sex" column matches that of the string "sex". When returning the list of records, the function will exclude the "sex" column from the records.

  Parameters
  ----------
  enrolment_by_age: 
      List of records

  sex:
    A string

  Returns
  -------
  list
      A list of records that matches the parameter "sex" in the "sex" column, exclude the sex column from this list

  Examples
  ----------
    >>> mf_enrolment = filter_gender(enrolment_data, "MF")
    >>> mf_enrolment
    [[1984, '17 YRS', 8710],
     [1984, '18 YRS', 3927],
     [...],
     [...],
     ...]

  """ 
  matched = []
  for data in enrolment_by_age:
    if data[2] == sex:
      matched.append([data[0],data[1],data[3]])
  return matched

def sum_by_year(enrolment):
  """
  This function add up the total enrolment of each year, regardless of age. Then it returns a list comprises of two integers, "year" and "total_enrolment".

  Parameters
  ----------
  enrolment: 
      List of records

  Returns
  -------
  list
      List of two integers,"year" and "total_enrolment".

  Examples
  --------
  >>> enrolment_by_year = sum_by_year(mf_enrolment)
  >>> enrolment_by_year
  [[1984, 21471],
   [1985, 24699],
   [...],
   [...],
   ...]
  """
# Type your code below
  current_year = enrolment[0][0]
  sum = [[current_year, 0]]
  for line in enrolment:
      if current_year == line[0]:
          sum[-1][1] += line[-1]
      else:
          current_year = line[0]
          sum.append([current_year, line[-1]])
  return sum

def write_csv(filename, header, data):
  """

  This function writes "header" , "data" and "filename" in CSV format to a file according to the parameters given and returns the number of lines written.

  Parameters
  ----------
  filename:
    A string denoting the name of the file written

  Header:
    A list containing the header of the file

  Data:
    Data written

  Returns
  -------
  integer
    The number of lines written

  Examples
  --------
  >>> filename = 'total-enrolment-by-year.csv'
    >>> header = ["year", "total_enrolment"]
    >>> write_csv(filename, header, enrolment_by_year)
    35
  """
  # Type your code below
  with open(filename,"w") as f:
    f.writelines(header)
    lines = 0
    for data_line in data:
      write_list = ""
      for d in data_line:
       write_list += f",{d}"
      f.writelines(write_list)
      lines += 1
    return lines

# head,enrolment_data = read_csv("pre-u-enrolment-by-age.csv")
# print(filter_gender(enrolment_data,"F"))

# a = a
# b = b
# with open("pre-u-enrolment-by-age.csv".w) as f:
#   f.write()

# print(read_csv("pre-u-enrolment-by-age.csv"))
# print(filter_gender(read_csv("pre-u-enrolment-by-age.csv"),"MF"))
# print(sum_by_year(read_csv("pre-u-enrolment-by-age.csv")))

