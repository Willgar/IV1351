package se.kth.iv1351.view;
import se.kth.iv1351.controller.Controller;
import se.kth.iv1351.model.InstrumentDTO;

import java.util.List;
import java.util.Scanner;

public class BlockingInterpreter {
    private static final String PROMPT = "> ";
    private final Scanner console = new Scanner(System.in);
    private Controller ctrl;
    private boolean keepReceivingCmds = false;

    /**
     * Creates a new instance that will use the specified controller for all operations.
     *
     * @param ctrl The controller used by this instance.
     */
    public BlockingInterpreter(Controller ctrl) {
        this.ctrl = ctrl;
    }

    /**
     * Stops the commend interpreter.
     */
    public void stop() {
        keepReceivingCmds = false;
    }

    /**
     * Interprets and performs user commands. This method will not return until the
     * UI has been stopped. The UI is stopped either when the user gives the
     * "quit" command, or when the method <code>stop()</code> is called.
     */
    public void handleCmds() {
        keepReceivingCmds = true;
        while (keepReceivingCmds) {
            try {
                CmdLine cmdLine = new CmdLine(readNextLine());
                switch (cmdLine.getCmd()) {
                    case HELP:
                        for (Command command : Command.values()) {
                            if (command == Command.ILLEGAL_COMMAND) {
                                continue;
                            }
                            System.out.println(command.toString().toLowerCase());
                        }
                        break;
                    case QUIT:
                        keepReceivingCmds = false;
                        break;
                    case RENT:
                        ctrl.rentInstrument(cmdLine.getParameter(0), cmdLine.getParameter(1));
                        break;
                    case END:
                        ctrl.terminateRental(cmdLine.getParameter(0));
                    case LIST:
                        List<? extends InstrumentDTO> instruments = null;
                        instruments = ctrl.listRentalInstruments();
                        if(cmdLine.getParameter(0).equals("")) {
                            for (InstrumentDTO instrument : instruments) {
                                System.out.println("Instrument ID " + instrument.getInstrumentID() + ", "
                                        + "Instrument Type: " + instrument.getInstrumentType() + ", "
                                        + "Monthly Price: " + instrument.getInstrumentMonthlyPrice() + ", "
                                        + "Instrument Brand: " + instrument.getInstrumentBrand());
                            }
                        } else{
                            for (InstrumentDTO instrument : instruments) {
                                if(cmdLine.getParameter(0).equals(instrument.getInstrumentType())) {
                                    System.out.println("Instrument ID " + instrument.getInstrumentID() + ", "
                                            + "Instrument Type: " + instrument.getInstrumentType() + ", "
                                            + "Monthly Price: " + instrument.getInstrumentMonthlyPrice() + ", "
                                            + "Instrument Brand: " + instrument.getInstrumentBrand());
                                }
                            }
                        }

                        break;
                    default:
                        System.out.println("illegal command");
                }
            } catch (Exception e) {
                System.out.println("Operation failed");
                System.out.println(e.getMessage());
                e.printStackTrace();
            }
        }
    }

    private String readNextLine() {
        System.out.print(PROMPT);
        return console.nextLine();
    }
}