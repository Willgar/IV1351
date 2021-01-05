package se.kth.iv1351.model;

public interface InstrumentDTO {
    /**
     * @return The Instrument ID
     */
    public String getInstrumentID();
    /**
     * @return The Instrument Type
     */
    public String getInstrumentType();
    /**
     * @return The Return Date
     */
    public String getReturnDate();
    /**
     * @return The Student ID
     */
    public String getStudentID();
    /**
     * @return The Instruments Monthly Price
     */
    public int getInstrumentMonthlyPrice();
    /**
     * @return The Instruments Brand
     */
    public String getInstrumentBrand();

}
