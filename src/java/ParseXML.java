import javax.xml.parsers.*;
import java.io.*;
import org.w3c.dom.*;

public class ParseXML {

    private static final String PATH_TO_XML = "src/xml/test.xml";

    public static void main(String[] args) throws Exception{
        ParseXML p = new ParseXML();
        p.parse("recipe");
    }

    public void parse(String attribute) throws Exception {

        File input = new File(PATH_TO_XML);
        DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
        Document doc = docBuilder.parse(input);
        NodeList ingredientList = doc.getElementsByTagName(attribute);
        for(int i = 0; i < ingredientList.getLength(); i++) {
            Element e = (Element) ingredientList.item(i);
            System.out.println(e.getAttribute("name"));
            for(int j = 0; j < e.getElementsByTagName("ingredient").getLength(); j++) {
                System.out.println(e.getElementsByTagName("ingredient").item(j).getTextContent());
            }
        }
    }
}
