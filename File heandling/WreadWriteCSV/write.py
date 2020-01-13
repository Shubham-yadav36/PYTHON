from csv import writer, DictWriter

with open("Data.csv", 'w', newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['name', 'country'])
    csv_writer.writerow(['Shubham', 'India'])
    csv_writer.writerow(['Raja', 'USA'])

with open("witedata.txt",'a',newline='') as f:
    csv_writer1 = DictWriter(f,fieldnames=["name","age"])
    csv_writer1.writeheader()
    csv_writer1.writerow({
        'name' : 'Shubham',
        'age' : '25'
    })
