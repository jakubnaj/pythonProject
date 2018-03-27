import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { Category } from '../../../navigation/models/category';
import { environment } from '../../../../environments/environment';

@Injectable()
export class CategoryService {

  constructor(private http: HttpClient) {}
  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(environment.endpoints.getCategories);
  }
}
