import java.util.Scanner;

public class Main {

  public static String ClassificaPacote(double peso){
    if (peso <= 3.0){
      return "Leve";
    }
    else if (peso <= 10.0){
      return "Médio";
    }
    else if (peso <= 100){
      return "Pesado";
    }
    else{
      return "Muito pesado";
    }
  }
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    double peso;
    System.out.print("Digite o peso do pacote: ");
    peso = sc.nextDouble();
    System.out.println("O pacote é " + ClassificaPacote(peso));
    
  }
}