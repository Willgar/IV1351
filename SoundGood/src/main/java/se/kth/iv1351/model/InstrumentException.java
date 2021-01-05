package se.kth.iv1351.model;

/**
 * Thrown when create, read or deletion of an instrument fails.
 */
public class InstrumentException extends Exception {
    /**
     * Creates a new instance using the reason.
      * @param reason The reason why it failed
     */
    public InstrumentException(String reason) {
        super(reason);
    }

    /**
     * Creates a new instance using the reason and the root cause of failure.
     * @param reason The reason why it failed
     * @param rootCause The exception which caused the exception to be thrown.
     */
    public InstrumentException(String reason, Throwable rootCause){
        super(reason, rootCause);
    }
}
