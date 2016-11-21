import re

pattern = re.compile(r'(?P<name>p[a-zA-Z]+)(?P<version>[0-9])')
results = pattern.search('python2')
print results
print results.groupdict()

a = re.compile(r"""\d +
                    \.
                    \d *
                """, re.X)

b = re.compile(r'(\w+[-\w]*)@([a-zA-Z0-9]+).(com|org|edu)')
results = b.search('chu-tian-shu_1981@heibanke2015.com')
#print results.group()

text = 'aaa@163.com chu-tian-shu_1981@heibanke2015.com abc-fff@xfd.org ccc_fd2@fff.edu aaa@111.com'
# print re.match(r"\w+[-\w]*@[a-zA-Z0-9]+.\'com\'|\'org\'|\'edu\'", text)
print re.findall(r'\w+[-\w]*@[a-zA-Z0-9]+\.com\b|\w+[-\w]*@[a-zA-Z0-9]+\.org\b|\w+[-\w]*@[a-zA-Z0-9]+\.edu\b', text)