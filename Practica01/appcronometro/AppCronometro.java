/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
*/
package appcronometro;

public class AppCronometro {

    public static int[] generarNumeros(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = (int)(Math.random() * 1_000_000); // 0..999999
        }
        return a;
    }

    // Ordenacion por seleccion
    public static void seleccion(int[] a) {
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if (a[j] < a[min]) min = j;
            }
            int tmp = a[i];
            a[i] = a[min];
            a[min] = tmp;
        }
    }

    public static void main(String[] args) {
        int[] datos = generarNumeros(100000);

        Cronometro c = new Cronometro();
        c.inicia();

        seleccion(datos);

        c.detener();

        System.out.println("Tiempo (ms): " + c.lapsoDeTiempo());
    }
}

