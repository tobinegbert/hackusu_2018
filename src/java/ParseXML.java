import javax.xml.parsers.*;
import java.io.*;
import org.w3c.dom.*;

public class ParseXML {

    private static final String PATH_TO_XML = "../xml/";

    public static void main(String[] args) {

    }

    public void parse() throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        StringBuilder xmlStringBuilder = new StringBuilder();
        xmlStringBuilder.append("<?xml version=\"1.0\"?> <class> </class>");
        ByteArrayInputStream input = new ByteArrayInputStream(
                xmlStringBuilder.toString().getBytes("UTF-8"));
        Document doc = builder.parse(input);
    }
}
