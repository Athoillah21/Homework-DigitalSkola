class StudentApp {
    
    public static void main(String[] args) {
        var Academician = new Academician("Athoillah",23);
        Academician.name = "Athoillah";
        Academician.age = 23;
        
        Student s = new Student();
        Academician.studentSubject("Matematika");
        s.studentSubject("Matematika");
    }
}