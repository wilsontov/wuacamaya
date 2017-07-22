package telpro.main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import telpro.views.FoldersSelect;

public class Main {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     * @throws java.lang.InterruptedException
     */
    public static void main(String[] args) throws IOException, InterruptedException {
        FoldersSelect fold = new FoldersSelect();
        fold.setVisible(true);
    }

    public static String startProcess(String path, String save_path) throws IOException, InterruptedException {
        ProcessBuilder pb = new ProcessBuilder(
                "/home/karther/juliapro/JuliaPro-0.5.2.2/Julia/bin/julia", // Path de Julia
                "/home/karther/Dropbox/TELEMEDICINE/telPro/Julia/background.jl", // Path del Script
                path, // Carpeta de imagenes
                save_path // Carpeta donde se guardan
        );
        Process process = pb.start();
                
        if (process.waitFor() > 0) {
            return output(process.getErrorStream());
        } else {
            return output(process.getInputStream());
        }     
        
    }
    
    private static String output(InputStream inputStream) throws IOException {
        StringBuilder sb = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(inputStream))) {
            String line = null;
            while ((line = br.readLine()) != null) {
                sb.append(line).append(System.getProperty("line.separator"));
            }
        }
        
        return sb.toString();
    }
}
