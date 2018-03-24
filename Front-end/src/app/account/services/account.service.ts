import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { User } from "../models/user";
import { environment } from "../../../environments/environment";

@Injectable()
export class AccountService {
  constructor(private http: HttpClient) {}
  registerUser(user: User) {
    return this.http.post(environment.endpoints.createUser, user);
  }
}
