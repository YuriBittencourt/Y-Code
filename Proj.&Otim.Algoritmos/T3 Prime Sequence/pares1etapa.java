public class pares1etapa {
	static boolean isPrime(int n) {
        if (n == 2) return true;
        if (n < 2 || n%2==0) return false;
        for (int i = 3; i*i<= n; i += 2)
            if (n % i == 0) return false;
        return true;
	}
	static boolean contains(int val, int arr[]){
		for (int num : arr){ 
				if (num==val) return true;
				if (num==0) return false; //após o 0 não teremos mais nada significativo.
		}
		return false;
	}
	
	static void montaSequencia(int sequence[], int n) {
		for(int i=1;i<=sequence.length;i++) {
			if(!contains(0,sequence)){
			    for (int s : sequence) {
                    		System.out.print(s + " ");
            	    	    }
			    System.out.println();
			    System.exit(0);	
			}
			if(contains(i,sequence) || (n!=0 && !isPrime(sequence[n-1]+i))) continue;
			sequence[n]=i;
			//System.out.println("["+n+"]= "+ i); //eh bom saber as mudancas
			montaSequencia(sequence,n+1);
			sequence[n]=0;
		}
	}
	
	public static void main(String Args[]){
		int size = Integer.parseInt(Args[0]);
		if(size<2){
		    System.out.println("Valor inválido");
		    return;    
		}
		int sequence[] = new int[size];
		montaSequencia(sequence,0);
		System.out.println("Não há sequência");        	    	   
	}
}