import java.io.*;

public class karatsuba {
	public static String strAdd(String a, String b) {
		String res="";
		String carry="0";
		String soma="";
		int diff=a.length()-b.length();
		if(diff!=0) {
			while(diff>0) {
				b="0"+b;
				diff--;
			}
			
			while(diff<0) {
				a="0"+a;
				diff++;
			}
		}
		for(int i=a.length()-1;i>=0;i--) {
			if(i==a.length()) {
				soma=(Integer.parseInt(a.substring(i))+Integer.parseInt(b.substring(i)))+"";
			}
			else
				soma=(Integer.parseInt(a.substring(i,i+1))+Integer.parseInt(b.substring(i,i+1))+ Integer.parseInt(carry))+"";
			
			if(soma.length()>1) {
				carry=soma.substring(0, 1);
				soma=soma.substring(1);
				
			}
			else carry="0";
			
			res=soma + res;
		}
		if(Integer.parseInt(carry)!=0)
			return carry + res;
		return res;
	}
	
	public static String strMultiply(String a, String b) {
	    if(greaterThan(b,a)) {
            String aux = a;
            a=b;
            b=aux;
        }
        long i = Integer.parseInt(b);
		String res="0";
		while(i>0){

		    res=strAdd(a,res);
		    i--;
        }
        return wipeZeros(res);
	}
	
	public static String strShift(String a, int b) {
		while (b>=1) {
			a=a+"0";
			b--;
		}
		return a;
	}
	
	public static String zeros(int a) {
		String z="";
		while(a>=1) {
			z="0"+z;
			a--;
		}
		return z;
	}

	public static boolean greaterThan(String a, String b){
	    a= wipeZeros(a);
	    b= wipeZeros(b);
	    if(a.length()>b.length()){
	        return true;
        }
        else if(a.length()<b.length()){
	        return false;
        }
        for (int i=0;i<a.length();i++){
	        if(Integer.parseInt(a.substring(i,i+1))>Integer.parseInt(b.substring(i,i+1))){
	            return true;
            }
            else if(Integer.parseInt(a.substring(i,i+1))<Integer.parseInt(b.substring(i,i+1))){
	            return false;
            }
        }
        return false; //são iguais.
    }

	public static String wipeZeros(String n){
		n=n.replaceAll("^0*","");
	    if(n.equals("")){
			return "0";
		}
		return n;
	}

	public static String strMinus(String a, String b) {
        // a-b requer que a>=b
        String res = "";
        int valor=0;
        int diff = a.length() - b.length();
        if (diff != 0) {
            while (diff > 0) {
                b = "0" + b;
                diff--;
            }

            while (diff < 0) {
                a = "0" + a;
                diff++;
            }
        }

        if (greaterThan(b, a)) throw new IllegalArgumentException("'a'deve ser maior que 'b'");
        boolean carry = false;
        for (int i = a.length()-1; i >=0; i--) {
            int aIndex, bIndex;

            if (i == a.length()) {
                aIndex=Integer.parseInt(a.substring(i));
                bIndex=Integer.parseInt(b.substring(i));
            }
            else {
                aIndex=Integer.parseInt(a.substring(i, i+1));
                bIndex=Integer.parseInt(b.substring(i, i+1));
            }
            if(carry) {
                if (aIndex > bIndex) {
                    res = (aIndex - bIndex - 1) + res;
                    carry = false;
                } else
                    if(aIndex <= bIndex){
                        res = (aIndex - bIndex + 9) + res;
                        //Errei bastante aqui, como já tem carry e vc está pedindo mais, obvio que n te vem 10, vem 9!!!
                    }
            }
            else {
                if (aIndex >= bIndex) {
                    res = (aIndex - bIndex) + res;
                }
                else {
                    res = (aIndex - bIndex + 10) + res;
                    carry = true;
                }
            }
        }
        return res;

	}

	public static String multKaratsuba(String a, String b) {
        if (wipeZeros(a).length() == 1 && wipeZeros(b).length() == 1)
            return wipeZeros(strMultiply(a, b));
            //return Integer.parseInt(wipeZeros(a))*Integer.parseInt(wipeZeros(b)) + "";
            //aqui o return vai ao gosto do fregues, ambos multiplicam.

        int shifts;
        if (a.length() > b.length()) {
            b = zeros(a.length() - b.length()) + b;
        } else
            a = zeros(b.length() - a.length()) + a;

        if (a.length() == b.length()) {
            if (a.length() % 2 != 0) {
                a = "0" + a;
                b = "0" + b;
            }
        }

        shifts = a.length() / 2;

        String aHI = a.substring(0, shifts);
        String aLO = a.substring(shifts);

        String bHI = b.substring(0, shifts);
        String bLO = b.substring(shifts);

        String abHI = multKaratsuba(aHI, bHI);
        String abLO = multKaratsuba(aLO, bLO);
        String middlePart = strMinus(strMinus(multKaratsuba(strAdd(aHI, aLO), strAdd(bHI, bLO)), abHI), abLO);

        return wipeZeros(strAdd(strShift(abHI, 2 * shifts), strAdd(strShift(middlePart, shifts), abLO)));
    }

	public static void main (String Args[]) {
	    try {
            BufferedReader scanner = new BufferedReader(new FileReader(new File("source.txt")));
            BufferedWriter ext = new BufferedWriter(new FileWriter(new File("saidaKaratsuba.txt")));

            for (String x = scanner.readLine(); x != null; x = scanner.readLine()){
                String s[]= x.split(" ");
                String res=multKaratsuba(s[0],s[1]);
                ext.write(res+"\n");
                }
                ext.close();
        }
        catch (Exception FileNotFoundException){
	        System.out.println("Arquivo nao encontrado. Abortando execucao");
	        return;
        }

    }
}
