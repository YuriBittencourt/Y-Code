public class RotaSimples {
    static long Mem[][][] = new long[50][50][50];

    public static void main(String args[]) {
        //preenchendo os eixos (dois eixos com valor 0)
        for(int i=0;i<Mem.length;i++)
            Mem[i][0][0]= Mem[0][i][0]= Mem[0][0][i]=1;

        //preenchendo planos 0 (seja x,y ou z=0)
        for(int i=1;i<Mem.length;i++)
            for (int j=1;j<Mem.length;j++)
                Mem[i][j][0] = Mem[0][i][j] = Mem[i][0][j]= Mem[i-1][j][0] + Mem[i][j-1][0] + Mem[i-1][j-1][0];


        //preenche o resto
        for(int x=1; x<Mem.length; x++)
            for (int y = 1; y < Mem.length; y++)
                for (int z = 1; z < Mem.length; z++)
                    Mem[x][y][z] = Mem[x - 1][y][z] +
                            Mem[x][y - 1][z] +
                            Mem[x][y][z - 1] +
                            Mem[x - 1][y - 1][z] +
                            Mem[x - 1][y][z - 1] +
                            Mem[x][y - 1][z - 1] +
                            Mem[x - 1][y - 1][z - 1];





        int arg1, arg2, arg3;
        arg1= Integer.parseInt(args[0]);
        arg2= Integer.parseInt(args[1]);
        arg3= Integer.parseInt(args[2]);
        System.out.println(Mem[arg1][arg2][arg3]);

        /* Bloco de controle para visualizar um pedaço da matriz, deixei ele pois talvez seja útil ao professor.
        for(int x=1; x<10; x++)
            for (int y = 1; y < 10; y++)
                for (int z = 1; z < 10; z++)
                    System.out.println("index(" + x + "," + y + "," + z +")" + Mem[x][y][z]);
        */
    }

}