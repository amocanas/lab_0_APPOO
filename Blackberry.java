public class Blackberry extends Mobile{  
    //Constructor to set properties/characteristics of object  
    Blackberry(String man, String os,String model, int cost){  
                    super(man, os, model, cost);  
                }  
    public String getModel(){  
        return "This is Blackberry-"+ model;  
    }  
}  