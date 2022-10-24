// // // Child Class
class Student extends Academician {
	String grade;
	
	// Constructor
	Student(String name, Integer age) {
		super(name, age);
		}

    // Override Methods
    void studentSubject() {
        super.studentSubject();
        System.out.println("I am a Student");
    }
}