#!/usr/bin/env python
# coding: utf-8

# ### Dictionaries
# - Dictionaries

# ### Dictionaries
# 
# - It works on the concept of Set Unique Data
# - Keys,values is the unique identifier for a value
# - Each key is separated from its values with colon(:)_
# - Each key and value is separated by comma(,)
# - Dictionaries enclosed with curly braces({})

# In[5]:


d1 = {"Name":"Gitam","EmailId":"gitam@gmail.com","Address":"Hyderabad"}
print(d1)


# In[6]:


d1["Name"]


# In[9]:


d1["EmailId"] = 'Gitam-python@gmail.com'


# In[12]:


d1['EmailId']


# In[20]:


del d1['Emailid']


# In[21]:


d1


# In[22]:


d1.keys() # returns the list of keys


# In[23]:


d1.items() # the list of tuples of keys and values


# ### Tuples
# - t1 parenthesis() li square brackets[]
# - Differences between list and tuples
#     -list are mutable- can be changed/modified
#        -Used to access modify,add,delete data
#  - tuples are immutable-cannot be changed
#        -Used to access data only

# In[25]:


t1 = (1,2,3,4,5,6)
t1
type(t1)


# ### Contact Application
# - Add contact
# - Search the contact
# - List all contacts
#     - name1 : phone1
#     - name2 : phone2
# - Modify the contact
# - Remove the contact
# - Import the contact

# In[29]:


# Add contact
contacts = {}
def addcontact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("Contact is details are added")
    else:
        print("Contact details already exists")
    return
addcontact('anuraag','182962654')
addcontact('aghvuy','862474673')
addcontact('anuraag','182962654')


# In[32]:


# Search for contacts details
def searchContact(name):
    if name in contacts:
        print(name," : ",contacts[name])
    else:
        print("%s does not exists" % name)
    return
searchContact('anuraag')
searchContact('vinay')
searchContact('vignesh')


# In[39]:


# Import new contacts
# Merge the contacts with existing one
def ImportContacts(newContacts):
    contacts.update(newContacts)
    print(len(newContacts.keys()),"Contacts added succesfully")
    return
newContacts={'Dinesh':8669886528,'pradeep':1245845684}
ImportContacts(newContacts)


# In[47]:


# Delete a contact
def deleteContacts(name):
    if name in contacts:
        del contacts[name]
        print(name,"delete succesfully")
    else:
        print(name,"not exists")
    return
deleteContacts('pradeep')


# In[42]:


contacts


# In[45]:


# Update the contact details
def deleteContact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"Update successfully")
    else:
        print(name,"Not exists")
    return
deleteContact('Dinesh',8669886528)
deleteContact('vinay',97987877787)


# In[3]:


li1=[1,2,3,4]
print("%d %d %d %d" % (li1[0],li1[1],li1[2],li1[3]))


# In[4]:


#String 

#classical version
li=["Python","Programming"]
print("%s %s"%(li[0],li[1]))


# In[5]:


li1 = [1,2,3,4]
print("%d %d %d %d" % (li1[0],li1[1],li1[2],li1[3]))


# In[6]:


print("{0} {1} {2} {3} ".format(li1[0],li1[1],li1[2],li1[3]))


# ### String Functions
# - Upper() - will convert given string into upper case
# - lower() - will convert given string into lower case

# In[7]:


s1='Gitam'
print(s1.upper())
print(s1.lower())


# ### Boolean Function(True and False)
# - islower() --True if the string is lower case/False if the string not in lower case
# - isupper --True if the string is upper case/False if the string not in lower case
# - istitle --True if the string follows titlr case/False
# - isalpha --True if the string contains alphabets
#  - isnumeric --True if the string contains only numbers/False

# In[12]:


s1='GITAM'
print(s1.islower())
print(s1.isupper())


# In[14]:


s2 = "Python Programming"
s3 = "python Programming"
print(s2.istitle())
print(s3.istitle())


# In[16]:


s2 = "Application1889"
s3 = 'PythonProgramming'
print(s2.isalpha())
print(s3.isalpha())


# In[18]:


s1 = "1234"
s2 = "Application1234"
print(s1.isnumeric())
print(s2.isnumeric())


# In[19]:


s1 = " "
s2 = "Py th on"
print(s1.isspace())
print(s2.isspace())


# ### String Methods
# - 1.join()--Method will concatinates the two strings
# - 2.spilt() --split() returns the list of strings separated by a whitespace
# - 3.replace() -- replaces the specific word/character with a new word

# In[34]:


s1 = 'Python'
print(" ".join(s1))


# In[22]:


s2 = "Python Programming Easy to learn"
print(",".join(s2))


# In[25]:


li = ['Python','Programming','Learn']
print(",".join(li))


# In[28]:


s2 = "Python Programming Easy to learn"
print(s2.split())


# In[30]:


s2 = "Python Programming Easy to learn"
print(s2.split('a'))


# In[31]:


s2 = "Python Programming Easy to learn"
li = s2.split()
print(li)
print(len(li))


# In[32]:


s2 = "Python Programming Easy to learn"
li = list(s2)
print(li)


# In[33]:


s2 = "Python Programming Easy to learn"
print(s2.replace("gra","Application"))


# In[ ]:




