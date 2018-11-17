import javax.xml.parsers.*;
import java.io.*;
import org.w3c.dom.*;

public class ParseXML {

    private static final String PATH_TO_XML = "test.xml";

    public static void main(String[] args) {
        try {
            ParseXML p = new ParseXML();
            p.parse();
        } catch (Exception e) {

        }

    }

    public void parse() throws Exception {

        File input = new File(PATH_TO_XML);
        if(input.canRead()) System.out.println("Good");
        DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
        Document doc = docBuilder.parse(input);
        NodeList ingredientList = doc.getElementsByTagName("student");
        for(int i = 0; i < ingredientList.getLength(); i++) {
            System.out.println(ingredientList.item(0));
        }
    }
}
