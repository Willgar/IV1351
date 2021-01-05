package se.kth.iv1351.startup;

import se.kth.iv1351.controller.Controller;
import se.kth.iv1351.integration.SoundGoodDBException;
import se.kth.iv1351.view.BlockingInterpreter;

/**
 * Starts the SoundGood Client.
 */
public class Main {
    public static void main(String[] args) {
        try {
            new BlockingInterpreter(new Controller()).handleCmds();
        } catch(SoundGoodDBException sgdbe) {
            System.out.println("Could not connect to Sound Good.");
            sgdbe.printStackTrace();
        }
    }
}
