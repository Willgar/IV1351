package se.kth.iv1351.integration;


public class SoundGoodDBException extends Exception {
    /**
     * Creates a new exception based on the cause
     * @param reason The cause of the exception
     */
    public SoundGoodDBException(String reason) {
        super(reason);
    }
    /**
     * Create a new instance thrown because of the specified reason and exception.
     *
     * @param reason    Why the exception was thrown.
     * @param rootCause The exception that caused this exception to be thrown.
     */
    public SoundGoodDBException(String reason, Throwable rootCause) {
        super(reason, rootCause);
    }
}
