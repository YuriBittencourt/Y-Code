
public class cidade {
	double x,y;
	String nome;
	
	public cidade(double x, double y, String nome) {
		this.x=x;
		this.y=y;
		this.nome=nome;
	}
	String textify() {
		return (x + " " + y + " " + nome);
	}

	String toPair(){
		return x + " " + y;
	}
	
	double dista(cidade c) {
		return	Math.sqrt((c.x - this.x)*(c.x - this.x) + (c.y - this.y)*(c.y - this.y));
	}
}
