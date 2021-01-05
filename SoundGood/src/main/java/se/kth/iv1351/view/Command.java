package se.kth.iv1351.view;

public enum Command {
    /**
     * Lists all existing accounts.
     */
    LIST,
    /**
     * Lists all commands.
     */
    HELP,
    /**
     * Leave the chat application.
     */
    QUIT,
    /**
     * Rents an instrument
     */
    RENT,
    /**
     * Terminates a rental
     */
    END,
    /**
     * None of the valid commands above was specified.
     */
    ILLEGAL_COMMAND
}
