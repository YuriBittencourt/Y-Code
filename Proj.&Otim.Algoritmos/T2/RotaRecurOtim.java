public class RotaRecurOtim {
    static long Mem[][][] = new long[50][50][50];
    public static long RotaRecursiva(int x, int y, int z) {
        if (x == 0 && y == 0 && z == 0) return 1;
        if (x<0 || y<0 || z<0) return 0;
        if (Mem[x][y][z]!=0) return Mem[x][y][z];
        Mem[x][y][z] =  RotaRecursiva(x - 1, y, z) +
                        RotaRecursiva(x, y - 1, z) +
                        RotaRecursiva(x, y, z - 1) +
                        RotaRecursiva(x - 1, y - 1, z) +
                        RotaRecursiva(x - 1, y, z - 1) +
                        RotaRecursiva(x, y - 1, z - 1) +
                        RotaRecursiva(x - 1, y - 1, z - 1);

        return Mem[x][y][z];
    }

    public static void main(String args[]) {
        int arg1, arg2, arg3;
        arg1= Integer.parseInt(args[0]);
        arg2= Integer.parseInt(args[1]);
        arg3= Integer.parseInt(args[2]);
        System.out.println(RotaRecursiva(arg1, arg2, arg3));
    }

}