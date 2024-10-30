# python-basic-lec13-oct-30-24

## subjects learned:

* functions:
    * function name must start with small letter and if contains more then 1 work use capital letters to separate the
      words
      ```
      def inputIntNumber(): # or input_int_number():
          ....    
      ``` 
    * all line below the def must indentations.
    * must call the function(outside the function). otherwise you just defined it and didn't use it:
       ```
      inputIntNumber()
       ```
    * import function from other file in the project:
        ```
      from main import inputIntNumber
       ```
    * can import the entire file:
         ```
      import main
      main.inputIntNumber()
       ```
    * function explanation: inside the function, must describe what the function does in short.
     ```
    def print_hello():
        """prints my first function """
        print("my first function")
    ```
    * function help(<file name>)/ help(<function>)- will display the explanation in the console.
    ```
    help(lec13)
    help(lec13)
  ```
        

## extra subjects:
* dunder(double underscore)- 
  * definition: Dunder variables define a contract between Python programmers and the Python interpreter.
  * for every running file the python defines a parameter __name__ with the value __main__, if you have import , the __name__ of the imported file is __file name__. 
  * therefore if you don't want to run stuff from the import file, you add:
    
```
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
```
see example in line 6 in lec13.py
  