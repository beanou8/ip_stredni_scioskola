export class Guest {
    private _firstName : string;
    private _lastName : string;
    private _dateOfBirth : Date;

    //Constructor
    constructor(firstName: string, lastName: string, dateOfBirth: Date) {
        this._firstName = firstName;
        this._lastName = lastName;
        this._dateOfBirth = dateOfBirth;
    }

    //Getters and Setters
    get firstName(): string {
        return this._firstName;
    }

    set firstName(value: string) {
        this._firstName = value;
    }

    get lastName(): string {
        return this._lastName;
    }

    set lastName(value: string) {
        this._lastName = value;
    }

    get dateOfBirth(): Date {
        return this._dateOfBirth;
    }

    set dateOfBirth(value: Date) {
        this._dateOfBirth = value;
    }
}