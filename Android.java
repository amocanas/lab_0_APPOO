public class Android extends Mobile{  
        //Constructor to set properties/characteristics of object  
        Android(String man, String os,String model, int cost){  
                super(man, os, model, cost);  
            }  
        //Method to get access Model property of Object  
        public String getModel(){  
            return "This is Android Mobile- " + model;  
        }  
}  