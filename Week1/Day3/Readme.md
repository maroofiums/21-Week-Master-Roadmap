# Day3

## **1. Classes and Objects**

* **Class**: Blueprint for objects. Think of it as a template.
* **Object**: An instance of a class. Each object can have its own data.

Example:

```python
class Student:
    pass  # Empty class for now
```

Now `Student` is a class, but it does nothing yet.

---

## **2. Attributes & Methods**

* **Attributes**: Variables that belong to an object (like name, age).
* **Methods**: Functions inside a class (like calculate grade).

---

## **3. `__init__` constructor**

`__init__` runs **automatically** when an object is created. We use it to initialize attributes.

```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name  # self.name is attribute
        self.age = age
        self.marks = marks
```

**Tip:** `self` represents the instance itself. Always include it in methods inside a class.

---

## **4. Adding a method to calculate grade**

Let’s add a method to calculate grades based on marks:

```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
```

---

## **5. Creating objects and printing details**

```python
# Creating student objects
student1 = Student("Ali", 16, 85)
student2 = Student("Sara", 17, 92)
student3 = Student("Ahmed", 15, 74)

# Printing details
students = [student1, student2, student3]

for s in students:
    print(f"Name: {s.name}, Age: {s.age}, Marks: {s.marks}, Grade: {s.calculate_grade()}")
```

**Output:**

```
Name: Ali, Age: 16, Marks: 85, Grade: A
Name: Sara, Age: 17, Marks: 92, Grade: A+
Name: Ahmed, Age: 15, Marks: 74, Grade: B
```

---

## **6. Inheritance Basics**

* Inheritance allows a class to **reuse code** from another class.
* Example: Let’s say we want a `CollegeStudent` that has all attributes of `Student` but also a `college_name`.

```python
class CollegeStudent(Student):
    def __init__(self, name, age, marks, college_name):
        super().__init__(name, age, marks)  # Call parent constructor
        self.college_name = college_name

# Create object
c_student = CollegeStudent("Zara", 18, 88, "ABC College")
print(f"{c_student.name}, {c_student.age}, {c_student.marks}, {c_student.calculate_grade()}, {c_student.college_name}")
```

**Output:**

```
Zara, 18, 88, A, ABC College
```

✅ Key takeaway: `super().__init__()` is how you **reuse parent class attributes**.

---

### **Honest Advice & Best Practices**

1. Always use `self` for attributes and methods.
2. Keep methods small and focused (like `calculate_grade`).
3. Use inheritance **only when needed**, don’t overcomplicate.
4. For multiple objects, store them in a **list or dictionary** to iterate easily.

---

### **Quick Summary / Tip**

* **Class = Blueprint**, **Object = Instance**
* `__init__` = Constructor, runs automatically
* **Attributes** store data, **Methods** do actions
* **Inheritance** = reuse & extend parent class
* Always think **“self” points to this specific object**

