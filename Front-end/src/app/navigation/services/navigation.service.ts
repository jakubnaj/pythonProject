import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Category } from "../models/category";
import { environment } from "../../../environments/environment";
import { Observable } from "rxjs/Observable";

@Injectable()
export class NavigationService {
  constructor(private http: HttpClient) {}
 
}
