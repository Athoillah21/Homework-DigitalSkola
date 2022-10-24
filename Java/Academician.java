// Parent Class
class Academician {
    String name;
    Integer age;

    // Constructor
    Academician(String name, Integer age){
        this.name = name;
        this.age = age;
    }

    // Methods
    void studentSubject(String subject){
        System.out.println("Name "+this.name+", Age "+this.age+", Subject "+subject);
    }
}