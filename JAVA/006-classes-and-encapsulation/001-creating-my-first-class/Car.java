import java.util.UUID;

/**
 * =================================
 * CORE OOP CONCEPTS
 * =================================
 *
 * 1. ENCAPSULATION
 * ----------------
 * ANALOGY: A car's dashboard. I use the pedals and steering wheel (public methods)
 * without needing to know about the complex engine (private data). This protects
 * the internal data and keeps things simple.
 *
 * 2. FINAL
 * --------
 * ANALOGY: A car's Vehicle Identification Number (VIN).
 * - CONCEPT: A `final` attribute is a constant that can only be assigned a value
 *   ONCE, typically when the object is created (in the constructor). Once set,
 *   it can never be changed.
 * - USAGE: It's perfect for values that should be immutable, like a unique ID,
 *   a birth date, or a serial number. You usually provide a getter but no setter.
 *
 */
public class Car {

    // Private fields: The internal data of my Car. Hidden from the outside.
    private String make;
    private String model;
    private int year;
    // A `final` attribute. It can only be set once. Like a car's VIN.
    private final String vin;

    // A static field. This belongs to the CLASS, not to any single object.
    private static int carCounter = 0;

    // Constructor: My blueprint for creating a new Car object and setting its
    // initial state.
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        // Assigning the final 'vin' field. This can only be done here!
        this.vin = UUID.randomUUID().toString();
        carCounter++; // Increment the shared counter every time a new car is created.
    }

    // --- PUBLIC INTERFACE (My "Dashboard") ---

    // Getters: Let me safely READ the private fields.
    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    // Getter for the final 'vin' field. Note there is no setter.
    public String getVin() {
        return vin;
    }

    // Setter: Lets me safely MODIFY the 'year'.
    // I can add validation here, e.g., if (year > 1886) { ... }
    public void setYear(int year) {
        this.year = year;
    }

    // A public method that uses the class's internal data to perform an action.
    public void displayInfo() {
        System.out.println("Car Info: " + year + " " + make + " " + model + " (VIN: " + vin + ")");
    }

    // A static method to access the static field.
    public static int getCarCounter() {
        return carCounter;
    }
}