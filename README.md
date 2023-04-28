# MentalHealthStudentPortal
*by Carvalheira, Ricardo; Min, James; Patel, Mihir*


## 1. Problem
The problem that our project aims to address is the lack of mental health support resources in schools. As reported by Delray Beach Psychiatrists, a significant percentage of schools do not have counselors, school psychologists, or social workers on staff to provide support to students who may be experiencing mental health challenges. With the increasing number of mental health issues among students, it is essential to provide a system that can help schools manage and track the mental health of their students effectively. Many schools do not have a system to accomplish that in place to address these concerns in a timely manner. 

## 2. Motivation
This lack of resources can leave students without access to the care they need, potentially exacerbating their mental health issues and impacting their academic performance. Public institutions can utilize our system to collect mental health surveys and gain insights into the overall health of the student body. This information can help schools identify and prioritize the most pressing issues and allocate resources effectively.

## 3. Features
The system being designed allows students to register and take mental health assessments,
after which they will be assigned to a mental health volunteer for further support. The system allows students to track their visits and compare past surveys, and volunteers to create records and provide direct assistance. The data structures are searchable and filterable, allowing for easy input and retrieval of patient data. However, the system's goal is not to provide diagnoses but rather connect students to
necessary resources and check self-progress, as diagnoses require trained and empathetic professionals:

1. Student Side:
    - **Search** - Students will be able to view their information (including name, email, phone number, address, school name, school year, date of birth) using their name, dob, address, phone, email, or a uniquely assigned ID.
  
   - **Insert** - When a new student accesses the website, they can create a record inside the portal if they have never provided information in the system.

   - **Delete** - A student can delete their information when they log into the portal. This is done so that all the records attached to that student are removed.

   - **Modify** - If a student wants to update their records in a while, they can do so by logging into the portal. They may also submit surveys on their current mental state that will update the student records on the urgency they need assistance.

2. Staff/Volunteer Side:
  
   - **Search** - Employees will be able to view information using their unique staff ID. They can also fetch a particular student record by using the student UD.

   - **Insert** - When a new student comes in, an employee can manually enter information and register on behalf of the student.

   - **Delete** - An Employee can delete a student’s information when they provide a student's ID. An employee won’t be able to delete their records (by design and to reduce complexity).

   - **Modify** - An Employee may also update students’ records by providing their uniquely assigned student ID.
 
## 4. Data
We are using randomly generated data based on real dataset examples to make up for the 100,000+ unique tuples. The fields in our data set will include: {Student ID: String, Email: String, Name: String, Phone Number: Integer, Age Group: String, Race Ethnicity: String, Sex: String, DOB: Date, Address: String, Survey Submitted: Date-Time (automatic on insertion), Area of Interest: String, Institution Name: String, Academic Level: String, GPA: String, Marital Status: String, Housing Condition: String, Family Size: String, Mother’s Education: String, Quantity of Visits: Integer, Employee ID: String (won’t be viewable on student’s side), Employee Name: String, Happiness Score: Float, Are you feeling depressed? - Have you ever been diagnosed with depression or anxiety before?: Boolean 

## 5. Tools/Languages/APIs/Libraries used
We used the Python programming language and the Flask web framework to develop the system. We implemented Hash Tables and B-trees to efficiently store and manage a fictional dataset.In addition to these, we used utility python packages such as pandas, time, datetime, csv, random, and data table and standard data containers such as data frames, dictionaries, lists and tuples. We are also using GitHub and Trello for checkpoints and project tracking. We also used R to create the fake data set. In R, we used the following libraries to assist generating the data: randomNames, openxlsx, data.table, tidyverse, generator, and leaflet. Lastly, we used a site called FakeNameGenerator to generate fake, yet believable, house addresses in the FL, USA.

## 6. Algorithms implemented
Hash tables and B-trees are both data structures that can be used to store information about students and their records. In a hash table, a built-in list data structure is used to implement separate chaining. This prevents collisions, which occur when two different keys are hashed to the same slot in the hash table. The slots of the hash table contain lists of key-value pairs, while B-trees contain dictionaries of key-value pairs. When a collision occurs, a new key-value pair is simply added to the list or node at the corresponding slot. Each slot in a hash table can contain multiple key-value pairs, and so collisions can be resolved by using a list data structure for separate chaining. For a B-tree, information is simply added in the correct position.
The advantage of using a list data structure for separate chaining is that it is simple to implement and can be used with any hashing function. Additionally, it allows for a high degree of flexibility, as the size of the lists can be adjusted based on the number of collisions that occur. On the other hand, using a dictionary to store node information inside the B-tree allows B-trees to be scaled to very large sizes. For example, if the student uses the mental health services again in the future, their information gets added to their respective node's dictionary. 

## 7. Additional Data Structures/Algorithms used:
None. 

## 8. Distribution of Responsibility and Roles:
Carvalheira, Ricardo: Responsible for Front-end Development and Design
Min, James: Responsible for Data Structure, and Research
Patel, Mihir: Responsible for Data Structure, and Data Transformation and Visualization (note, visualization is a "stretch goal.") 

## 9. Any changes the group made after the proposal?
We chose not to let the students view their past visits and assigned volunteer/staff using name, dob, address, phone, email, and ID to deliver a Minimum Viable Product. For simplicity’s sake, we search using their student ID only and retrieve the student's information only without past visits and volunteer/staff. Also, employees will only search using the student ID as these are unique to one student, and no bulk search will be allowed in this MVP. For deleting and modifying, we will no longer search using name, dob, address, phone, or email because when the student logs in, they already provided their ID. So, for a better user experience, we are not asking again for their personal information to perform any operations.

## 10. Big O worst case time complexity analysis of the major functions/features you implemented:” 
In **Hash Map**, There are five major functions: _hash, get, exist, put, and remove:

    1. _hash: O(1) - this function computes the hash of the key using the selected hashing function, which is a constant time operation.
    
    2. get: O(k) - this function needs to traverse the built-in list in the slot corresponding to the hash of the key, where k is the length of this list. In the worst-case scenario, when all the keys in the table collide and end up in the same slot, the time complexity becomes O(n), where n is the total number of entries in the table.

    3. exist: O(k) - this function is similar to get, but it returns a boolean value indicating the key's existstance in the table. Therefore, the time complexity is the same as get.

    4. put: O(k) - this function needs to check if the key already exists in the table before inserting a new (key, value) pair. It requires traversing the built-in list in the corresponding slot, which has a time complexity of O(k), where k is the length of the list. In the worst-case scenario, when all the keys in the table collide and end up in the same slot, the time complexity becomes O(n), where n is the total number of entries in the table. When the table needs to be expanded, the time complexity becomes O(n), where n is the total number of entries in the table.
    
    5. remove: O(k) - this function needs to search for the (key, value) pair corresponding to the key in the linked list in the corresponding slot, which has a time complexity of O(k), where k is the length of the list. In the worst-case scenario, when all the keys in the table collide and end up in the same slot, the time complexity becomes O(n), where n is the total number of entries in the table. When the table needs to be shrunk, the time complexity becomes O(n), where n is the total number of entries in the table.

Overall, the worst-case time complexity of the HashTable class is O(n), where n is the total number of entries in the table, in case all the keys collide and end up in the same slot. However, in practice, this is unlikely to happen, and the time complexity of the major functions is expected to be O(1) or O(k), where k is the number of entries in the slot corresponding to the hash of the key.

In **B-Tree**, There are five major functions: get_keys_value, update_keys, pull_node_info, search, insert_nonfull, split_child, insert, delete_internal_node,delete_predecessor_node,delete_successor_node, delete_merge, delete_sibling and delete:

    1. get_keys_value(): O(log n)
    
    2. update_keys(): O(log n)
    
    3. pull_node_info(): O(log n)
    
    4. search(): O(log n) - The `search` method is used to search for a key in the B-tree. The method also starts from the root node and recursively descends through the tree until it finds the appropriate node that contains the key. The time complexity of this operation is also O(log n) where n is the number of keys in the tree.
    5. insert_nonfull(): O(log n)

    6. split_child(): O(log n)

    7. insert(): O(log n)- The `insert` method is used to insert a new key into the B-tree. The method starts from the root node and recursively descends through the tree until it finds an appropriate leaf node for insertion. The time complexity of this operation is O(log n) where n is the number of keys in the tree. This is because the B-tree maintains a balanced tree structure, where each level of the tree has a fixed number of keys.

    8. delete_internal_node(): O(log n)

    9. delete_predecessor_node(): O(log n)

    10. delete_successor_node(): O(log n)

    11. delete_merge(): O(log n)

    12. delete_sibling(): O(log n)

    13. delete(): O(log n) - The `delete` method is used to delete a key from the B-tree. The method starts from the root node and recursively descends through the tree until it finds the appropriate node that contains the key. Once the node is found, the method uses different techniques such as merging or borrowing keys from siblings to maintain the balance of the tree. The time complexity of this operation is also O(log n) where n is the number of keys in the tree.

The time complexity of each function is determined by the number of nodes that need to be traversed in order to find the desired node or key. For example, the __init__() function only needs to traverse one node, so its time complexity is O(1). The get_keys_value() function needs to traverse the root node and all of its children in order to find the desired key, so its time complexity is O(log n). The update_keys() function needs to traverse the root node and all of its children in order to find the desired key, and then it needs to update the value of the key, so its time complexity is also O(log n).
The other functions all have similar time complexities, as they all need to traverse the root node and all of its children in order to find the desired node or key. The only exception is the delete() function, which can have a time complexity of O(n) if the key to be deleted is not found in the root node. In this case, the function will need to traverse all of the nodes in the tree in order to find the key.


## 11. Some examples shown with **B-Tree**

1. *Student Registration*
    ![image](https://user-images.githubusercontent.com/47681434/235155679-d2ce08d0-448d-48fb-a0d6-76d5f4311fa5.png)


2. *Student Profile*
    ![image](https://user-images.githubusercontent.com/47681434/235157586-33fd1374-163b-4092-8520-01a52740a16c.png)


3. *Student Profile > Complete Survey*
    ![image](https://user-images.githubusercontent.com/47681434/235160823-c4d51c62-80c3-4780-95ac-b8e3bc4ac449.png)


4. *Student Profile > Update Profile Info*
    ![image](https://user-images.githubusercontent.com/47681434/235162593-eebe847b-15fc-4c82-b259-9c4622472021.png)
    
    ![image](https://user-images.githubusercontent.com/47681434/235164353-29e7af6c-2db0-474c-9fa6-ac449e6a24fb.png)


5. *Student Profile > Delete Profile*
    ![image](https://user-images.githubusercontent.com/47681434/235163599-b11bc1af-4115-4b7e-a14e-8c51124447cb.png)

