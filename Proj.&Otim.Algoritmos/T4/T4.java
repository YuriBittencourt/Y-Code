import java.io.*;
import java.util.Random;
import java.util.List;
import java.util.ArrayList;

public class T4 {
	cidade[] cidades;
	List<cidade[]> pop;
	//para todo elemento em lst: somar com o proximo, ultimo soma com o index 0;
	public double distanciaTotal(cidade[] arr) {
		double soma=0;
		for(int i=0;i<arr.length;i++) {
			//System.out.println(lst.get(i).getNome() + " viaja Para " + lst.get((i+1)%lst.size()).getNome());
			soma+=arr[i].dista(arr[(i+1)%arr.length]);
		}
		return soma;
	}
	//troca lst[a] com lst[b]
	public cidade[] troca(cidade[] arr, int a, int b){
		cidade[] arrB = arr.clone();
		arrB[a]=arr[b];
		arrB[b]=arr[a];
		return arrB;
	}

	public void addPop(cidade[] c){
	    if (pop.size()<200) {
	        pop.add(c);
	        return;
        }
        int aux = findWorstAmongPop();
        if(distanciaTotal(pop.get(aux))<=distanciaTotal(c)) return;
        pop.remove(aux);
        pop.add(c);
    }
    public  void reverse(){
	    cidade aux;
	    for (int i=0; i<cidades.length/2;i++){
	        aux = cidades[i];
	        cidades[i]=cidades[cidades.length-1-i];
	        cidades[cidades.length-1-i]=aux;
        }
    }
    public int findWorstAmongPop(){
    	int aux=0;
        for (int i=1; i<pop.size();i++) {
            if(distanciaTotal(pop.get(i))>distanciaTotal(pop.get(aux))) aux=i;
        }
        return aux;
    }
    public int findBestAmongPop(){
    	int aux=0;
        for (int i=1; i<pop.size();i++) {
            if(distanciaTotal(pop.get(i))<=distanciaTotal(pop.get(aux))) aux=i;
        }
        return aux;
    }

	public void printViagem(cidade[] arr) {
		for(int i=0;i<arr.length;i++) {
			System.out.println(arr[i].nome + " viaja Para " + arr[(i+1)%arr.length].nome);
		}
	}
	public void salva()throws IOException {
		cidade[] c = pop.get(findBestAmongPop());
		if(c==null) return;
		BufferedWriter bw = new BufferedWriter(new FileWriter("resultFor" + c.length));
		bw.write(c.length + "\n");
		for (cidade city: c) {
			bw.write(city.textify()+ "\n");
		}
		bw.close();
	}

	public T4(String file[]) throws IOException {
        pop = new ArrayList<cidade[]>();
		BufferedReader br = new BufferedReader(new FileReader(file[0]));
		int tam = Integer.parseInt(br.readLine());
		cidades = new cidade[tam];
		String line;
		int index=0;
		while ((line = br.readLine()) != null) {
			String[] split = line.split(" ");
			cidades[index]=new cidade(Double.parseDouble(split[0]), Double.parseDouble(split[1]), split[2]);
			index++;
		}
		br.close();
		System.out.println("Leitura Realizada com sucesso!");
	}
	public void exec() throws IOException {
		cidade[] viagem;
		int tam = cidades.length;
		Random seed = new Random(tam*System.nanoTime()*7);
		int noChanges=0;
		int best = -1;
		System.out.println("Iniciado com: " + distanciaTotal(cidades));
		while(true) {
			int aRand = seed.nextInt(tam);
			int bRand = seed.nextInt(tam);
			if(aRand==bRand) {
			    continue;
            }
			viagem=troca(cidades, aRand, bRand);
			if(distanciaTotal(cidades)>distanciaTotal(viagem)) { 
				cidades=viagem.clone();
                if(!pop.isEmpty()) salva();
                noChanges=0;
    			continue;
			}
            if(noChanges==10000){
                addPop(cidades);
                reverse();
                cidades=troca(cidades, aRand, bRand);
			    noChanges=0;    			
            } 
            if(!pop.isEmpty() && best != findBestAmongPop()){ 
            	System.out.println(distanciaTotal(pop.get(best = findBestAmongPop())));
            }
            noChanges++;
            
        }
	}
}
